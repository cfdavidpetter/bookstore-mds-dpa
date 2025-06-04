import { IBook } from "@/core/models/book.model";
import { BookService } from "@/core/services/book.service";
import { PaginatedResponse } from "@/shared/components/pagination-view/types";
import { useRef, useState } from "react";

export function useBooks() {
  const [response, setResponse] = useState<PaginatedResponse<IBook>>({
    data: [],
    total: 0,
    per_page: 0,
    current_page: 0,
    next_page: 0,
    from: 0,
    previous_page: 0,
    last_page: 0,
  });
  const loading = useRef(true);
  const firstRender = useRef(true);
  const [error, setError] = useState<string | null>(null);

  async function fetchItems(page: number = 1) {
    try {
      loading.current = true;
      const response = await new BookService().list(page);
      setResponse(response as PaginatedResponse<IBook>);
      loading.current = false;
    } catch (error) {
      setError(error as string);
      loading.current = false;
    }
  }

  return {
    firstRender,
    loading,
    response,
    error,
    fetchItems,
  };
}
