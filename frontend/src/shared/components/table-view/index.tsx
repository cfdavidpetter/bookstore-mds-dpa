import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "../ui/table";
import { TableProps } from "./types";

export default function TableView<T>({
  data,
  columns,
  actions,
}: TableProps<T>) {
  return (
    <Table>
      {data.length === 0 && <TableCaption>No data found</TableCaption>}
      <TableHeader>
        <TableRow>
          {columns.map((column) => (
            <TableHead key={column.header}>{column.header}</TableHead>
          ))}
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.map((row, index) => (
          <TableRow key={index}>
            {columns.map((column) => (
              <TableCell key={column.header}>
                {row[column.accessor as keyof T] as string}
              </TableCell>
            ))}
            {actions && <TableCell>{actions}</TableCell>}
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
