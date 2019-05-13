import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../service/provider.service';
import { IBook,IUser ,IUserProfile,IQuotation} from '../models/model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public books:IBook[]=[];
  public logged=false;
  public login:any= '';
  public password:any='';
  public userProfile:IUserProfile[]=[];
  public userbooks:IBook[];


  
  constructor( private provider:ProviderService) { }

  ngOnInit() {
    const token=localStorage.getItem('token');
    if(token){
      this.logged=true;
    }
    if(this.logged ){
      
      this.provider.UserProfileDetail().then(res=>{
        console.log(res)
        this.userProfile=res;
        this.userbooks=this.userProfile[0].book;
        console.log(this.userbooks)
      });

      // console.log('logged')
      // this.provider.getBooks().then(res =>{
      //   this.books = res;
      // });
    }
  }
  auth() {
    if (this.login !== '' && this.password !== '') {
      console.log("asd")
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
  logout(){
    this.provider.logout().then(res=>{
      localStorage.clear();
      this.logged = false;
    })
  }
}
