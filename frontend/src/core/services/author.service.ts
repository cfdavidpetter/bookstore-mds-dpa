import { IAuthor } from "../models/author.model";
import { apiEndpoint } from "../constants";
import { requests } from "@/shared/lib/requests";
import { PaginatedResponse } from "@/shared/components/pagination-view/types";

export class AuthorService {
  list(page: number = 1, filters?: string): Promise<PaginatedResponse<IAuthor>> {
    let url = `${apiEndpoint.Authors}?page=${page}`;
    if (filters) {
      url += `&filters=${filters}`;
    }
    return requests.get(url).then((r: PaginatedResponse<IAuthor>) => r);
  }
}
