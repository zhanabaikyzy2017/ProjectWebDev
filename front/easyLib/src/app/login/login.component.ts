import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../service/provider.service';
import { IBook,IUser } from '../models/model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public books:IBook[]=[];
  public logged=false;
  public login:string="";
  public password:string="";
  
  constructor( private provider:ProviderService) { }

  ngOnInit() {
    const token=localStorage.getItem('token');
    if(token){
      this.logged=true;
    }
    if(this.logged ){
      console.log('logged')
      this.provider.getBooks().then(res =>{
        this.books = res;
      });
    }
  }
  auth() {
    console.log(this.login+" "+this.password);
    if (this.login !== '' && this.password !== '') {
        this.provider.auth(this.login,this.password).then(res => {
        localStorage.setItem('token', res.token);
        console.log(res);
        this.logged = true;
        this.provider.getBooks().then(r => {
          this.books = r;
        });
      });
    }
  }
}
