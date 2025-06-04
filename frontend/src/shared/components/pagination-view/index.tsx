import {
  Pagination,
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  PaginationNext,
  PaginationPrevious,
} from "../ui/pagination";
import { PaginatedResponse } from "./types";

export default function PaginationView<T>(
  response: PaginatedResponse<T>,
  fetchItems: (page: number, filters?: string) => void,
  filters: string
) {
  return (
    <Pagination>
      <PaginationContent>
        <PaginationItem>
          <PaginationPrevious href="#" onClick={() => fetchItems(response.previous_page, filters)} /> 
        </PaginationItem>
        {response.current_page > 2 && (
          <PaginationItem>
            <PaginationLink href="#" onClick={() => fetchItems(1, filters)}>
              <PaginationEllipsis />
            </PaginationLink>
          </PaginationItem>
        )}
        {response.current_page > 1 && (
          <PaginationItem>
            <PaginationLink
              href="#"
              onClick={() => fetchItems(response.current_page - 1, filters)}
            >
              {response.current_page - 1}
            </PaginationLink>
          </PaginationItem>
        )}
        <PaginationItem>
          <PaginationLink href="#" className="bg-black text-white">
            {response.current_page}
          </PaginationLink>
        </PaginationItem>
        {response.current_page < response.last_page && (
          <PaginationItem>
            <PaginationLink
              href="#"
              onClick={() => fetchItems(response.current_page + 1, filters)}
            >
              {response.current_page + 1}
            </PaginationLink>
          </PaginationItem>
        )}
        {response.current_page < response.last_page - 1 && (
          <PaginationItem>
            <PaginationLink href="#" onClick={() => fetchItems(response.last_page, filters)}>
              <PaginationEllipsis />
            </PaginationLink>
          </PaginationItem>
        )}
        <PaginationItem>
          <PaginationNext href="#" onClick={() => fetchItems(response.next_page, filters)} />
        </PaginationItem>
      </PaginationContent>
    </Pagination>
  );
}
