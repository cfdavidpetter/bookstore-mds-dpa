"use client"

import React, { useEffect, useState } from 'react';

interface Book {
  id: number;
  author: {
    id: number;
    title: string;
    biography?: string;
  };
  title: string;
}

export default function Home() {
  const [nameFilter, setNameFilter] = useState("");
  const [stateFilter, setStateFilter] = useState("");
  const [docNumberFilter, setDocNumberFilter] = useState("");
  const [documents, setDocuments] = useState<Book[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:7721/api/v1/books');
        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();
        setDocuments(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const filteredDocs = documents.filter((doc) => {
    return (
      doc.author.title.toLowerCase().includes(nameFilter.toLowerCase()) &&
      doc.title.toLowerCase().includes(stateFilter.toLowerCase()) &&
      doc.author.biography?.toLowerCase().includes(docNumberFilter.toLowerCase())
    );
  });

  if (loading) return <div>Loading documents...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div style={{ padding: "20px" }}>
      <h1>Document Finder</h1>
      <div>
        <label>Autor: </label>
        <input
          type="text"
          value={nameFilter}
          onChange={(e) => setNameFilter(e.target.value)}
        />
      </div>
      <div>
        <label>Livro: </label>
        <input
          type="text"
          value={stateFilter}
          onChange={(e) => setStateFilter(e.target.value)}
        />
      </div>
      <div>
        <label>Biografia: </label>
        <input
          type="text"
          value={docNumberFilter}
          onChange={(e) => setDocNumberFilter(e.target.value)}
        />
      </div>

      <table style={{ marginTop: "20px", border: "1px solid black" }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Autor</th>
            <th>Livro</th>
            <th>Biografia</th>
          </tr>
        </thead>
        <tbody>
          {filteredDocs.map((doc) => (
            <tr key={doc.id}>
              <td>{doc.id}</td>
              <td>{doc.author.title}</td>
              <td>{doc.title}</td>
              <td>{doc.author.biography}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

