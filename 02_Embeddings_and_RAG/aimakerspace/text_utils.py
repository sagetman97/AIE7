import os
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime


class TextFileLoader:
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.metadata = []
        self.path = path
        self.encoding = encoding

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path) and self.path.endswith(".txt"):
            self.load_file()
        else:
            raise ValueError(
                "Provided path is neither a valid directory nor a .txt file."
            )

    def load_file(self):
        with open(self.path, "r", encoding=self.encoding) as f:
            content = f.read()
            self.documents.append(content)
            
            # Generate metadata for the file
            file_metadata = {
                "source_file": self.path,
                "file_size": len(content),
                "created_at": datetime.now().isoformat(),
                "file_type": "txt",
                "encoding": self.encoding
            }
            self.metadata.append(file_metadata)

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding=self.encoding) as f:
                        content = f.read()
                        self.documents.append(content)
                        
                        # Generate metadata for each file
                        file_metadata = {
                            "source_file": file_path,
                            "file_name": file,
                            "file_size": len(content),
                            "created_at": datetime.now().isoformat(),
                            "file_type": "txt",
                            "encoding": self.encoding,
                            "relative_path": os.path.relpath(file_path, self.path)
                        }
                        self.metadata.append(file_metadata)

    def load_documents(self):
        self.load()
        return self.documents

    def load_documents_with_metadata(self) -> Tuple[List[str], List[Dict[str, Any]]]:
        """Load documents and return both content and metadata."""
        self.load()
        return self.documents, self.metadata


class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str, metadata: Optional[Dict[str, Any]] = None) -> Tuple[List[str], List[Dict[str, Any]]]:
        """Split text into chunks with metadata for each chunk."""
        chunks = []
        chunk_metadata = []
        
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunk = text[i : i + self.chunk_size]
            chunks.append(chunk)
            
            # Create metadata for this chunk
            chunk_meta = {
                "chunk_index": len(chunks) - 1,
                "start_position": i,
                "end_position": min(i + self.chunk_size, len(text)),
                "chunk_size": len(chunk),
                "created_at": datetime.now().isoformat()
            }
            
            # Inherit metadata from parent document if provided
            if metadata:
                chunk_meta.update(metadata)
                chunk_meta["parent_metadata"] = metadata
            
            chunk_metadata.append(chunk_meta)
        
        return chunks, chunk_metadata

    def split_texts(self, texts: List[str], metadata_list: Optional[List[Dict[str, Any]]] = None) -> Tuple[List[str], List[Dict[str, Any]]]:
        """Split multiple texts into chunks with metadata."""
        all_chunks = []
        all_metadata = []
        
        for i, text in enumerate(texts):
            metadata = metadata_list[i] if metadata_list and i < len(metadata_list) else None
            chunks, chunk_metadata = self.split(text, metadata)
            all_chunks.extend(chunks)
            all_metadata.extend(chunk_metadata)
        
        return all_chunks, all_metadata

    def split_with_metadata(self, texts: List[str], metadata_list: Optional[List[Dict[str, Any]]] = None) -> Tuple[List[str], List[Dict[str, Any]]]:
        """Alias for split_texts for clarity."""
        return self.split_texts(texts, metadata_list)


if __name__ == "__main__":
    # Test with metadata support
    loader = TextFileLoader("data/KingLear.txt")
    documents, doc_metadata = loader.load_documents_with_metadata()
    
    splitter = CharacterTextSplitter()
    chunks, chunk_metadata = splitter.split_with_metadata(documents, doc_metadata)
    
    print(f"Loaded {len(documents)} documents")
    print(f"Created {len(chunks)} chunks")
    print(f"Sample chunk metadata: {chunk_metadata[0] if chunk_metadata else 'No metadata'}")
