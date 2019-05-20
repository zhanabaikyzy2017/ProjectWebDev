import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../service/provider.service';
import { IBook,ICategory, IAuthor, IUserProfile } from '../models/model';
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public categories: ICategory[]=[];
  public authors: IAuthor[]=[];
  public books:IBook[]=[];
  public selectedCategoryBooks:IBook[];
  public selected=false;
  public authorSelected=false;
  public selectedAuthorBooks:IBook[];
  public cuProfile:IUserProfile;
  constructor(private provider:ProviderService) { }

  ngOnInit() {
    this.provider.getCategories().then(res =>{
      this.categories = res;
    });
    this.provider.getAuthors().then(res=>{
      this.authors=res;
    });
    this.provider.getCurUP().then(res=>{
      this.cuProfile=res;
    })
    this.provider.getBooks().then(res=>{
      this.books=res;
    });
  }
  getSelectedGenreBooks(category:ICategory){
    this.provider.getOneGenreBooks(category).then(res=>{
      this.selectedCategoryBooks=res;
      this.selected=true;
      console.log(res);
    })
  }
  getSelectedAuthorBooks(author:IAuthor){
    this.provider.getOneAuthorBooks(author).then(res=>{
      this.selectedAuthorBooks=res;
      this.authorSelected=true;
      console.log(res)
    })
  }
  back(){
    this.selected=false;
  }
  backForAuthor(){
    this.authorSelected=false;
  }
  
}
