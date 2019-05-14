import { Component, OnInit } from '@angular/core';
import { ICategory } from '../models/model';
import { ProviderService } from '../service/provider.service';

@Component({
  selector: 'app-one-genre',
  templateUrl: './one-genre.component.html',
  styleUrls: ['./one-genre.component.css']
})
export class OneGenreComponent implements OnInit {
  public selectedGenre:ICategory;
  constructor(private provider:ProviderService) { }

  ngOnInit() {
    this.provider.getOneGenreBooks(this.selectedGenre)
  }

}
