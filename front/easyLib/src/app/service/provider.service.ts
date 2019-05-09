import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MainService } from './main.service';
import {IAuthor,IBook,ICategory,IPublisher,IQuotation,IUser,IUserProfile,IAuthResponse} from '../models/model'

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  constructor(http:HttpClient) {
    super(http)
  }
  
  getBooks():Promise<IBook[]>{
    return this.get(`http://localhost:8000/api/books/`,{})
  }
  getCategories():Promise<ICategory[]>{
    return this.get(`http://localhost:8000/api/categories/`,{})
  }
  auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post(`http://localhost:8000/main/login/`, {
    username: login,
    password: password
  });
}
}
