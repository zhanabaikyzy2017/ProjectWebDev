import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MainService } from './main.service';
import {IAuthor,IBook,ICategory,IPublisher,IQuotation,IUser,IUserProfile} from '../models/models'

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http)
  }
}
