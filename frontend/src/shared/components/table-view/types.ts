export type Column<T> = {
  header: string;
  accessor: keyof T;
};

export type TableProps<T> = {
  data: T[];
  columns: Column<T>[];
  actions?: React.ReactNode;
};
