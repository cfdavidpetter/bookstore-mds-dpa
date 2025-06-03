import { PaginatedResponse } from "@/shared/lib/pagination";
import { requests } from "@/shared/lib/requests";
import { IBook } from "../models/book.model";
import { apiEndpoint } from "../constants";

export class BookService {
  list(): Promise<PaginatedResponse<IBook>> {
    return requests.get(`${apiEndpoint.Books}`).then((r: PaginatedResponse<IBook>) => r);
  }
}
