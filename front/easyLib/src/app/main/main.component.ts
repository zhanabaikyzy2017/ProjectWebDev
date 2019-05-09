import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../service/provider.service';
import { IBook,ICategory, IAuthor } from '../models/model';
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public categories: ICategory[]=[];
  public authors: IAuthor[]=[];
  public books:IBook[]=[];
  constructor(private provider:ProviderService) { }

  ngOnInit() {
    this.provider.getCategories().then(res =>{
      this.categories = res;
    });
    this.provider.getAuthors().then(res=>{
      this.authors=res;
    });
    this.provider.getBooks().then(res=>{
      this.books=res;
    });
  }

}
