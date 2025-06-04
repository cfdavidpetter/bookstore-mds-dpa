export interface Link {
  url: string | null;
  label: string;
  active: boolean;
}

export interface PaginatedResponse<T> {
  data: T[];
  total: number;
  per_page: number;
  from: number;
  current_page: number;
  next_page: number;
  previous_page: number;
  last_page: number;
  first_page_url?: string;
  last_page_url?: string;
  links?: Link[];
  next_page_url?: string;
  prev_page_url?: string;
}
