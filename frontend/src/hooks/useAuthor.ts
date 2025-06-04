import { IAuthor } from "@/core/models/author.model";
import { AuthorService } from "@/core/services/author.service";
import { PaginatedResponse } from "@/shared/components/pagination-view/types";
import { useRef, useState, useCallback } from "react";

export function useAuthors() {
  const [response, setResponse] = useState<PaginatedResponse<IAuthor>>({
    data: [],
    total: 0,
    per_page: 0,
    current_page: 0,
    next_page: 0,
    from: 0,
    previous_page: 0,
    last_page: 0,
  });
  const filters = useRef("");
  const loading = useRef(true);
  const firstRender = useRef(true);
  const [error, setError] = useState<string | null>(null);

  const fetchItems = useCallback(async (page: number = 1, filters?: string) => {
    try {
      loading.current = true;
      const response = await new AuthorService().list(page, filters);
      setResponse(response as PaginatedResponse<IAuthor>);
      loading.current = false;
    } catch (error) {
      setError(error as string);
      loading.current = false;
    }
  }, []);

  const fetchItemsWithFilters = useCallback((newFilters: string) => {
    if (newFilters) {
      filters.current = newFilters;
      fetchItems(1, newFilters);
    }
  }, []);

  const resetFilters = useCallback(() => {
    filters.current = "";
    fetchItems(1);
  }, []);

  return {
    filters,
    firstRender,
    loading,
    response,
    error,
    fetchItems,
    fetchItemsWithFilters,
    resetFilters,
  };
}
