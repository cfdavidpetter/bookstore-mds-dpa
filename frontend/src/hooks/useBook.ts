import { IBook } from "@/core/models/book.model";
import { BookService } from "@/core/services/book.service";
import { useEffect, useRef } from "react";
import { useState } from "react";

export function useBooks() {
  const isFirstRender = useRef(true);
  const [items, setItems] = useState<IBook[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function fetchItems() {
    console.log('Fetching items...');
    setLoading(true);
    try {
      const response = await new BookService().list();
      console.log('Response:', response);
      setItems(response.data);
    } catch (error) {
      setError(error as string);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    if (isFirstRender.current) {
      isFirstRender.current = false;
      fetchItems();
    }
  }, []);

  return { items, loading, error };
}