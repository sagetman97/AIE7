import numpy as np
from collections import defaultdict
from typing import List, Tuple, Callable, Dict, Any, Optional, Union
from aimakerspace.openai_utils.embedding import EmbeddingModel
import asyncio
from datetime import datetime


def cosine_similarity(vector_a: np.array, vector_b: np.array) -> float:
    """Computes the cosine similarity between two vectors."""
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    return dot_product / (norm_a * norm_b)


class VectorDatabase:
    def __init__(self, embedding_model: Optional[EmbeddingModel] = None):
        # Store both vectors and metadata
        self.vectors = defaultdict(np.array)
        self.metadata = defaultdict(dict)
        self.embedding_model = embedding_model or EmbeddingModel()

    def insert(self, key: str, vector: np.array, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Insert a vector with optional metadata."""
        self.vectors[key] = vector
        if metadata is not None:
            self.metadata[key] = metadata.copy()
        else:
            self.metadata[key] = {}

    def insert_with_metadata(self, text: str, vector: np.array, metadata: Dict[str, Any]) -> None:
        """Insert a vector with required metadata."""
        self.insert(text, vector, metadata)

    def search(
        self,
        query_vector: np.array,
        k: int,
        distance_measure: Callable = cosine_similarity,
        include_metadata: bool = False,
    ) -> Union[List[Tuple[str, float]], List[Tuple[str, float, Dict[str, Any]]]]:
        """Search for similar vectors with optional metadata."""
        scores = [
            (key, distance_measure(query_vector, vector))
            for key, vector in self.vectors.items()
        ]
        sorted_results = sorted(scores, key=lambda x: x[1], reverse=True)[:k]
        
        if include_metadata:
            return [(key, score, self.metadata[key]) for key, score in sorted_results]
        return sorted_results

    def search_by_text(
        self,
        query_text: str,
        k: int,
        distance_measure: Callable = cosine_similarity,
        return_as_text: bool = False,
        include_metadata: bool = False,
    ) -> Union[List[Tuple[str, float]], List[str], List[Tuple[str, float, Dict[str, Any]]]]:
        """Search by text query with optional metadata."""
        query_vector = self.embedding_model.get_embedding(query_text)
        results = self.search(query_vector, k, distance_measure, include_metadata)
        
        if return_as_text:
            return [result[0] for result in results]
        return results

    def retrieve_from_key(self, key: str, include_metadata: bool = False) -> Union[np.array, Tuple[np.array, Dict[str, Any]]]:
        """Retrieve vector and optionally metadata by key."""
        vector = self.vectors.get(key, None)
        if vector is None:
            return None
        
        if include_metadata:
            return vector, self.metadata[key]
        return vector

    def get_metadata(self, key: str) -> Optional[Dict[str, Any]]:
        """Get metadata for a specific key."""
        return self.metadata.get(key, None)

    def update_metadata(self, key: str, metadata: Dict[str, Any]) -> bool:
        """Update metadata for an existing key."""
        if key in self.vectors:
            self.metadata[key].update(metadata)
            return True
        return False

    def filter_by_metadata(self, filter_func: Callable[[Dict[str, Any]], bool]) -> List[str]:
        """Filter keys based on metadata criteria."""
        return [key for key, meta in self.metadata.items() if filter_func(meta)]

    def search_with_metadata_filter(
        self,
        query_text: str,
        k: int,
        metadata_filter: Optional[Callable[[Dict[str, Any]], bool]] = None,
        distance_measure: Callable = cosine_similarity,
        include_metadata: bool = False,
    ) -> Union[List[Tuple[str, float]], List[Tuple[str, float, Dict[str, Any]]]]:
        """Search with optional metadata filtering."""
        query_vector = self.embedding_model.get_embedding(query_text)
        
        # Apply metadata filter if provided
        if metadata_filter:
            filtered_keys = self.filter_by_metadata(metadata_filter)
            scores = [
                (key, distance_measure(query_vector, self.vectors[key]))
                for key in filtered_keys
            ]
        else:
            scores = [
                (key, distance_measure(query_vector, vector))
                for key, vector in self.vectors.items()
            ]
        
        sorted_results = sorted(scores, key=lambda x: x[1], reverse=True)[:k]
        
        if include_metadata:
            return [(key, score, self.metadata[key]) for key, score in sorted_results]
        return sorted_results

    async def abuild_from_list(self, list_of_text: List[str], metadata_list: Optional[List[Dict[str, Any]]] = None) -> "VectorDatabase":
        """Build database from list of texts with optional metadata."""
        embeddings = await self.embedding_model.async_get_embeddings(list_of_text)
        
        for i, (text, embedding) in enumerate(zip(list_of_text, embeddings)):
            metadata = metadata_list[i] if metadata_list and i < len(metadata_list) else {}
            self.insert(text, np.array(embedding), metadata)
        
        return self

    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the database."""
        total_vectors = len(self.vectors)
        vectors_with_metadata = sum(1 for meta in self.metadata.values() if meta)
        
        # Collect metadata field statistics
        metadata_fields = set()
        for meta in self.metadata.values():
            metadata_fields.update(meta.keys())
        
        return {
            "total_vectors": total_vectors,
            "vectors_with_metadata": vectors_with_metadata,
            "metadata_fields": list(metadata_fields),
            "metadata_coverage": vectors_with_metadata / total_vectors if total_vectors > 0 else 0
        }

    def export_metadata(self) -> Dict[str, Dict[str, Any]]:
        """Export all metadata."""
        return dict(self.metadata)

    def import_metadata(self, metadata_dict: Dict[str, Dict[str, Any]]) -> None:
        """Import metadata for existing keys."""
        for key, metadata in metadata_dict.items():
            if key in self.vectors:
                self.metadata[key] = metadata


if __name__ == "__main__":
    # Example usage with metadata
    list_of_text = [
        "I like to eat broccoli and bananas.",
        "I ate a banana and spinach smoothie for breakfast.",
        "Chinchillas and kittens are cute.",
        "My sister adopted a kitten yesterday.",
        "Look at this cute hamster munching on a piece of broccoli.",
    ]
    
    # Create metadata for each text
    metadata_list = [
        {"source": "food_blog", "category": "nutrition", "timestamp": datetime.now().isoformat()},
        {"source": "food_blog", "category": "nutrition", "timestamp": datetime.now().isoformat()},
        {"source": "pet_blog", "category": "animals", "timestamp": datetime.now().isoformat()},
        {"source": "pet_blog", "category": "animals", "timestamp": datetime.now().isoformat()},
        {"source": "pet_blog", "category": "animals", "timestamp": datetime.now().isoformat()},
    ]

    vector_db = VectorDatabase()
    vector_db = asyncio.run(vector_db.abuild_from_list(list_of_text, metadata_list))
    
    # Test search with metadata
    k = 2
    searched_vector = vector_db.search_by_text("I think fruit is awesome!", k=k, include_metadata=True)
    print(f"Closest {k} vector(s) with metadata:", searched_vector)
    
    # Test metadata filtering
    nutrition_results = vector_db.search_with_metadata_filter(
        "I think fruit is awesome!", 
        k=3, 
        metadata_filter=lambda meta: meta.get("category") == "nutrition",
        include_metadata=True
    )
    print(f"Nutrition-related results: {nutrition_results}")
    
    # Test statistics
    stats = vector_db.get_stats()
    print(f"Database stats: {stats}")
