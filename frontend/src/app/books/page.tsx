"use client";

import { useEffect } from "react";
import { IBook } from "@/core/models/book.model";
import TableView from "@/shared/components/table-view";
import { Column } from "@/shared/components/table-view/types";
import PaginationView from "@/shared/components/pagination-view";
import FilterView from "@/shared/components/filter-view";
import { useBooks } from "@/hooks/useBook";

export default function Books() {
  const { firstRender, response, loading, error, fetchItems } = useBooks();

  useEffect(() => {
    if (firstRender.current) {
      fetchItems();
      firstRender.current = false;
    }
  }, [firstRender, fetchItems]);

  return (
    <div className="flex flex-col p-4">
      <h1 className="text-2xl font-bold">Books</h1>
      {loading.current && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      { !loading.current && (
        <>
          <FilterView />
          <div className="flex justify-between">
            <TableView<IBook>
              data={response.data}
              columns={
                [
                  { header: "Name", accessor: "title" },
                  { header: "Author", accessor: "author.title" },
                  { header: "ISBN-13", accessor: "isbn13" },
                  { header: "ISBN-10", accessor: "isbn10" },
                  { header: "Format", accessor: "format" },
                  { header: "Publisher", accessor: "publisher" },
                  { header: "Publication Date", accessor: "pubdate" },
                ] as Column<IBook>[]
              }
            />
          </div>
          <div className="mt-4">
            {PaginationView<IBook>(response, fetchItems)}
          </div>
        </>
      )}
    </div>
  );
}
