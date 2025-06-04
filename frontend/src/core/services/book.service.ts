import { IBook } from "../models/book.model";
import { apiEndpoint } from "../constants";
import { requests } from "@/shared/lib/requests";
import { PaginatedResponse } from "@/shared/components/pagination-view/types";

export class BookService {
  list(page: number = 1, filters?: string): Promise<PaginatedResponse<IBook>> {
    let url = `${apiEndpoint.Books}?page=${page}`;
    if (filters) {
      url += `&filters=${filters}`;
    }
    return requests.get(url).then((r: PaginatedResponse<IBook>) => r);
  }
}
