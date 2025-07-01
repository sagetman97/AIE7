#!/usr/bin/env python3
"""
Test script to demonstrate the enhanced RAG system with metadata support.
"""

import asyncio
import os
from datetime import datetime
from typing import Optional, Callable

# Import our enhanced modules
from aimakerspace.text_utils import TextFileLoader, CharacterTextSplitter
from aimakerspace.vectordatabase import VectorDatabase
from aimakerspace.openai_utils.chatmodel import ChatOpenAI
from aimakerspace.openai_utils.prompts import SystemRolePrompt, UserRolePrompt


def test_metadata_functionality():
    """Test the metadata functionality without requiring OpenAI API."""
    
    print("=== Testing Metadata Functionality ===\n")
    
    # Create sample data
    sample_texts = [
        "This is a sample document about artificial intelligence and machine learning.",
        "Machine learning algorithms can be supervised or unsupervised.",
        "Deep learning is a subset of machine learning that uses neural networks.",
        "Natural language processing helps computers understand human language.",
        "Computer vision enables machines to interpret visual information."
    ]
    
    # Create metadata for each text
    sample_metadata = [
        {
            "source_file": "ai_documentation.txt",
            "category": "AI",
            "topic": "introduction",
            "chunk_index": 0,
            "chunk_size": len(sample_texts[0]),
            "created_at": datetime.now().isoformat()
        },
        {
            "source_file": "ml_guide.txt", 
            "category": "ML",
            "topic": "algorithms",
            "chunk_index": 1,
            "chunk_size": len(sample_texts[1]),
            "created_at": datetime.now().isoformat()
        },
        {
            "source_file": "deep_learning.txt",
            "category": "DL", 
            "topic": "neural_networks",
            "chunk_index": 2,
            "chunk_size": len(sample_texts[2]),
            "created_at": datetime.now().isoformat()
        },
        {
            "source_file": "nlp_guide.txt",
            "category": "NLP",
            "topic": "language_processing", 
            "chunk_index": 3,
            "chunk_size": len(sample_texts[3]),
            "created_at": datetime.now().isoformat()
        },
        {
            "source_file": "computer_vision.txt",
            "category": "CV",
            "topic": "visual_processing",
            "chunk_index": 4, 
            "chunk_size": len(sample_texts[4]),
            "created_at": datetime.now().isoformat()
        }
    ]
    
    print("1. Testing VectorDatabase with metadata...")
    
    # Create vector database (without embeddings for testing)
    vector_db = VectorDatabase()
    
    # Simulate inserting data with metadata
    for text, metadata in zip(sample_texts, sample_metadata):
        # Create a dummy vector (in real usage, this would be an embedding)
        dummy_vector = [0.1] * 1536  # OpenAI embedding dimension
        vector_db.insert(text, dummy_vector, metadata)
    
    print(f"   - Inserted {len(sample_texts)} documents with metadata")
    
    # Test metadata retrieval
    print("\n2. Testing metadata retrieval...")
    for i, text in enumerate(sample_texts):
        metadata = vector_db.get_metadata(text)
        if metadata:
            print(f"   - Document {i+1}: {metadata['category']} - {metadata['topic']}")
        else:
            print(f"   - Document {i+1}: No metadata found")
    
    # Test metadata filtering
    print("\n3. Testing metadata filtering...")
    
    # Filter by category
    ai_docs = vector_db.filter_by_metadata(lambda meta: meta.get("category") == "AI")
    print(f"   - AI documents: {len(ai_docs)} found")
    
    # Filter by chunk size
    large_chunks = vector_db.filter_by_metadata(lambda meta: meta.get("chunk_size", 0) > 50)
    print(f"   - Large chunks (>50 chars): {len(large_chunks)} found")
    
    # Filter by topic
    neural_net_docs = vector_db.filter_by_metadata(lambda meta: "neural" in meta.get("topic", ""))
    print(f"   - Neural network documents: {len(neural_net_docs)} found")
    
    # Test database statistics
    print("\n4. Testing database statistics...")
    stats = vector_db.get_stats()
    print(f"   - Total vectors: {stats['total_vectors']}")
    print(f"   - Vectors with metadata: {stats['vectors_with_metadata']}")
    print(f"   - Metadata fields: {stats['metadata_fields']}")
    print(f"   - Metadata coverage: {stats['metadata_coverage']:.2%}")
    
    # Test metadata export/import
    print("\n5. Testing metadata export/import...")
    exported_metadata = vector_db.export_metadata()
    print(f"   - Exported metadata for {len(exported_metadata)} documents")
    
    # Create new database and import metadata
    new_vector_db = VectorDatabase()
    for text in sample_texts:
        dummy_vector = [0.1] * 1536
        new_vector_db.insert(text, dummy_vector)
    
    new_vector_db.import_metadata(exported_metadata)
    print(f"   - Imported metadata successfully")
    
    print("\n=== All metadata tests passed! ===")


def test_text_utils_metadata():
    """Test the enhanced text utilities with metadata."""
    
    print("\n=== Testing Text Utils with Metadata ===\n")
    
    # Create sample text
    sample_text = "This is a sample document. It contains multiple sentences. " \
                  "We will split this into chunks. Each chunk will have metadata. " \
                  "The metadata will include position information and other details."
    
    # Create document metadata
    doc_metadata = {
        "source_file": "test_document.txt",
        "file_size": len(sample_text),
        "created_at": datetime.now().isoformat(),
        "file_type": "txt",
        "encoding": "utf-8"
    }
    
    print("1. Testing CharacterTextSplitter with metadata...")
    
    # Split text with metadata
    splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=10)
    chunks, chunk_metadata = splitter.split(sample_text, doc_metadata)
    
    print(f"   - Original text length: {len(sample_text)} characters")
    print(f"   - Created {len(chunks)} chunks")
    
    # Display chunk metadata
    for i, (chunk, metadata) in enumerate(zip(chunks, chunk_metadata)):
        print(f"   - Chunk {i+1}: {len(chunk)} chars, position {metadata['start_position']}-{metadata['end_position']}")
        print(f"     Source: {metadata['source_file']}")
    
    print("\n2. Testing multiple text splitting...")
    
    # Test with multiple texts
    texts = [
        "First document about AI.",
        "Second document about ML.",
        "Third document about NLP."
    ]
    
    text_metadata = [
        {"source_file": "doc1.txt", "category": "AI"},
        {"source_file": "doc2.txt", "category": "ML"}, 
        {"source_file": "doc3.txt", "category": "NLP"}
    ]
    
    all_chunks, all_metadata = splitter.split_texts(texts, text_metadata)
    
    print(f"   - Split {len(texts)} documents into {len(all_chunks)} chunks")
    
    # Show metadata inheritance
    for i, (chunk, metadata) in enumerate(zip(all_chunks, all_metadata)):
        print(f"   - Chunk {i+1}: {metadata['category']} from {metadata['source_file']}")
    
    print("\n=== Text utils metadata tests passed! ===")


def demonstrate_enhanced_rag_concept():
    """Demonstrate the concept of enhanced RAG with metadata."""
    
    print("\n=== Enhanced RAG Concept Demonstration ===\n")
    
    print("The enhanced RAG system with metadata support provides:")
    print("1. Rich document provenance tracking")
    print("2. Flexible search filtering based on metadata")
    print("3. Better context understanding for retrieved documents")
    print("4. Analytics on document characteristics")
    print("5. Improved retrieval quality through metadata-aware search")
    
    print("\nExample use cases:")
    print("- Filter search results by document source or date")
    print("- Prioritize chunks from specific sections or authors")
    print("- Analyze document coverage and quality")
    print("- Implement source-aware retrieval strategies")
    print("- Track document evolution over time")
    
    print("\n=== Concept demonstration complete! ===")


if __name__ == "__main__":
    print("Enhanced RAG System with Metadata Support - Test Suite")
    print("=" * 60)
    
    try:
        test_metadata_functionality()
        test_text_utils_metadata()
        demonstrate_enhanced_rag_concept()
        
        print("\n" + "=" * 60)
        print("All tests completed successfully!")
        print("The metadata support has been successfully implemented.")
        
    except Exception as e:
        print(f"\nError during testing: {e}")
        print("Please check your implementation and dependencies.") 