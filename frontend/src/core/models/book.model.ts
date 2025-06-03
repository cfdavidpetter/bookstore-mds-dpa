import { IBase } from "./base.model";
import { IAuthor } from "./author.model";
import { ISubject } from "./subject.model";

export enum IBookFormat {
  PAPERBACK = "Paperback",
  HARDCOVER = "Hardcover",
  LIBRARY_BINDING = "Library Binding",
  COMPACT_DISC = "Compact Disc",
  MASS_MARKET_PAPERBACK = "Mass Market Paperback",
  OTHER_FORMAT = "Other Format",
  MULTIMEDIA = "Multimedia",
}

export interface IBook extends IBase {
  author: IAuthor;
  authors?: IAuthor[];
  isbn13: number;
  isbn10: string;
  price?: number;
  format: IBookFormat;
  publisher: string;
  pubdate: string;
  edition?: string;
  subjects?: ISubject[];
  lexile?: string;
  pages?: number;
  dimensions?: string;
  overview?: string;
  excerpt?: string;
  synopsis?: string;
  toc?: string;
  editorial_reviews?: string;
}
