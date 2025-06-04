"use client";

import { useEffect } from "react";
import { IAuthor } from "@/core/models/author.model";
import TableView from "@/shared/components/table-view";
import { Column } from "@/shared/components/table-view/types";
import PaginationView from "@/shared/components/pagination-view";
import FilterView from "@/shared/components/filter-view";
import { useAuthors } from "@/hooks/useAuthor";

export default function Books() {
  const {
    firstRender,
    response,
    loading,
    error,
    filters,
    fetchItems,
    fetchItemsWithFilters,
    resetFilters,
  } = useAuthors();

  useEffect(() => {
    if (firstRender.current) {
      fetchItems();
      firstRender.current = false;
    }
  }, [fetchItems, firstRender]);

  return (
    <div className="flex flex-col p-4">
      <h1 className="text-2xl font-bold">Authors</h1>
      {loading.current && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      {!loading.current && (
        <>
          <FilterView
            inputsData={[
              {
                label: "Name",
                type: "text",
                placeholder: "Name",
                value: "",
                column: "title",
              },
              {
                label: "Slug",
                type: "text",
                placeholder: "Slug",
                value: "",
                column: "slug",
              },
              {
                label: "Biography",
                type: "text",
                placeholder: "Biography",
                value: "",
                column: "biography",
              },
            ]}
            setFilters={fetchItemsWithFilters}
            resetFilters={resetFilters}
          />
          <div className="flex justify-between">
            <TableView<IAuthor>
              data={response.data}
              columns={
                [
                  { header: "Name", accessor: "title" },
                  { header: "Slug", accessor: "slug" },
                  { header: "Biography", accessor: "biography" },
                ] as Column<IAuthor>[]
              }
            />
          </div>
          <div className="mt-4">
            {PaginationView<IAuthor>(response, fetchItems, filters.current)}
          </div>
        </>
      )}
    </div>
  );
}
