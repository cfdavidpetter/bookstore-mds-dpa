"use client";

import { IBook } from "@/core/models/book.model";
import TableView from "@/shared/components/table-view";
import { Column } from "@/shared/components/table-view/types";
import { useBooks } from "@/hooks/useBook";

export default function Books() {
  const { items, loading, error } = useBooks();

  const columns = [
    { header: "Name", accessor: "title" },
    { header: "Author", accessor: "author.title" },
    { header: "ISBN-13", accessor: "isbn13" },
    { header: "ISBN-10", accessor: "isbn10" },
    { header: "Format", accessor: "format" },
    { header: "Publisher", accessor: "publisher" },
    { header: "Publication Date", accessor: "pubdate" },
  ];

  return (
    <div>
      <h1>Books</h1>
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      <TableView<IBook> data={items} columns={columns as Column<IBook>[]} />
    </div>
  );
}
