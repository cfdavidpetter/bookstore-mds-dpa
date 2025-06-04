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

const getNestedValue = <T extends Record<string, unknown>>(obj: T, path: string): string | number | null => {
  const parts = path.split('.');
  const value = parts.reduce<unknown>((acc, part) => {
    if (acc && typeof acc === 'object' && part in (acc as Record<string, unknown>)) {
      return (acc as Record<string, unknown>)[part];
    }
    return null;
  }, obj);
  return value as string | number | null;
}

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
                {getNestedValue(row as Record<string, unknown>, column.accessor as string)}
              </TableCell>
            ))}
            {actions && <TableCell>{actions}</TableCell>}
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
