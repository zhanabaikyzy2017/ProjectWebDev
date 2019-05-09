import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../service/provider.service';
import { IBook,ICategory } from '../models/model';
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public categories: ICategory[]=[];
  constructor(private provider:ProviderService) { }

  ngOnInit() {
    this.provider.getCategories().then(res =>{
      this.categories = res;
    });
  }

}
