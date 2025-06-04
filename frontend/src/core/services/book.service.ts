import { IBook } from "../models/book.model";
import { apiEndpoint } from "../constants";
import { requests } from "@/shared/lib/requests";
import { PaginatedResponse } from "@/shared/components/pagination-view/types";

export class BookService {
  list(page: number = 1): Promise<PaginatedResponse<IBook>> {
    return requests.get(`${apiEndpoint.Books}?page=${page}`).then((r: PaginatedResponse<IBook>) => r);
  }
}
