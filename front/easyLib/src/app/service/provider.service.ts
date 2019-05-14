import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MainService } from './main.service';
import {IAuthor,IBook,ICategory,IPublisher,IUser,IUserProfile,IAuthResponse} from '../models/model'

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
  getAuthors():Promise<IAuthor[]>{
    return this.get(`http://localhost:8000/api/authors/`,{})
  }
  auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post(`http://localhost:8000/api/login/`, {
    username: login,
    password: password
  });
  }
  logout():Promise<any>{
    return this.post('http://localhost:8000/api/logout/',{})
  }
  UserProfileDetail():Promise<IUserProfile>{
    return this.get('http://localhost:8000/api/user_profiles/1',{
    });
  }
  getOneGenreBooks(category:ICategory):Promise<IBook[]>{
    return this.get(`http://localhost:8000/api/categories/${category.id}/books`,{})
  }
  getOneAuthorBooks(author:IAuthor):Promise<IBook[]>{
    return this.get(`http://localhost:8000/api/authors/${author.id}/books`,{})
  }
  getSelectedGenre(category:ICategory):Promise<ICategory>{
    return this.get(`http://localhost:8000/api/categories/${category.id}`,{})
  }
  getSelectedAuthor(author:IAuthor):Promise<IAuthor>{
    return this.get(`http://localhost:8000/api/authors/${author.id}`,{})
  }
  getCurUP():Promise<IUserProfile>{
    return this.get(`http://localhost:8000/api/this_user`,{})
  }
  createBook(book: IBook): Promise<IBook> {
    return this.post(`http://localhost:8000/api/categories/${book.category.id}/books/${book.author.id}/`, {
      title: book.title,
      // category:book.category,
      description:book.description,
      year:book.year,
      // author: book.author,
      page_amount:book.page_amount,
      // added_by:book.added_by,
      // image:book.image
    });
  }
  getUserBook(user_profile:IUserProfile):Promise<IBook[]>{
    return this.get(`http://localhost:8000/api/user_profile/${user_profile.id}/books`,{})
  }
  createCategory(name: any): Promise<ICategory> {
    return this.post('http://localhost:8000/api/categories/', {
      name: name,
    });
  }
  createAuthor(name: string,surname:string,date_of_birth:string,date_of_death:string): Promise<IAuthor> {
    return this.post(`http://localhost:8000/api/authors/`, {
      name: name,
      surname:surname,
      date_of_birth:date_of_birth,
      date_of_death:date_of_death
    });
  }
  getSelectedBook(book:IBook):Promise<IBook>{
    return this.get( `http://localhost:8000/api/books/${book.id}/`,{})
  }
  deleteBook(book:IBook):Promise<any>{
    return this.delet( `http://localhost:8000/api/books/${book.id}/`,{})
  }
  deleteAuthor(author:IAuthor):Promise<any>{
    return this.delet(`http://localhost:8000/api/authors/${author.id}`,{})
  }
  deleteGenre(genre:ICategory):Promise<any>{
    return this.delet(`http://localhost:8000/api/categories/${genre.id}`,{})
  }
  signup(login:string,password:string,email:string):Promise<IUser>{
    return this.post(`http://localhost:8000/api/signup/`,{
      username:login,
      password:password,
      email:email
    });
  }
}
