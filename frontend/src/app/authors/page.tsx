"use client";

import { IAuthor } from "@/core/models/author.model";
import TableView from "@/shared/components/table-view";
import { Column } from "@/shared/components/table-view/types";

export default function Authors() {
  const columns = [
    { header: "Name", accessor: "title" },
    { header: "Biography", accessor: "biography" },
  ];

  const data: IAuthor[] = [
    { title: "John Doe", biography: "John Doe is a software engineer" },
    { title: "Jane Doe", biography: "Jane Doe is a software engineer" },
  ];

  return (
    <div>
      <h1>Authors</h1>
      <TableView<IAuthor> data={data} columns={columns as Column<IAuthor>[]} />
    </div>
  );
}
