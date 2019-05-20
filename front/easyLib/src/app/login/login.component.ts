import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../service/provider.service';
import { IBook,IUser ,IUserProfile,ICategory,IAuthor} from '../models/model';



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
  public userProfile:IUserProfile;
  public userbooks:IBook[];
  public genres:ICategory[]=[];
  public authors:IAuthor[]=[];
  public selectedGenre:ICategory;
  public selectedAuthor:IAuthor;
  public genreclicked=false;
  public authorclicked=false;
  public bookcliked=false;
  public reviewclicked=false;
  public currentup:IUserProfile;
  public name:any='';
  public bookId:number;
  public bookName:any='';
  public bookDescription:any='';
  public bookPages:any='';
  public bookYear:any='';
  public is_staff:boolean;
  public signed = false;
  public aname:string;
  public asurname:string;
  public adb:any='';
  public add:any='';

  public slogin:any='';
  public spassword:any='';
  public semail:any='';
  public selectedBook:IBook;
  public globalName:string;
  public noacc=false;

 
  constructor( private provider:ProviderService) { }

  ngOnInit() {
    const token=localStorage.getItem('token');
    if(token){
      this.logged=true;
    }
    if(this.logged){
      this.provider.getCurUP().then(res=>{
        this.currentup=res;//Userprofile
        console.log(res);
        this.provider.getUserBook(this.currentup).then(r => {
          this.books = r;
          console.log(this.currentup);
        });
      })

      this.provider.UserProfileDetail().then(res=>{
        this.userProfile=res;
        console.log(this.userProfile)
      });
      this.provider.getCategories().then(res=>{
        this.genres=res;
      })
      this.provider.getAuthors().then(res=>{
        console.log(res)
        this.authors=res;
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
        console.log(res.is_staff);
        this.logged = true;
         this.is_staff = res.is_staff
        // this.provider.getUserBook(this.currentup).then(r => {
        //   this.books = r;
        //   console.log(r);
        // });
        
      });
    }
  }
  logout(){
    this.provider.logout().then(res=>{
      localStorage.clear();
      this.logged = false;
      this.is_staff=false;
    })
  }
  getSelBook(book:IBook){
    this.provider.getSelectedBook(book).then(res=>{
      this.selectedBook=res;
      console.log("ok");
      this.globalName=this.selectedBook.title;
    })
  }
  getSelGenre(category:ICategory){
    this.provider.getSelectedGenre(category).then(res=>{
      this.selectedGenre=res;
      console.log("ok");
      this.globalName=this.selectedGenre.name;
    })
  }
  noaccount(){
    this.noacc=true;
  }
  getSelAuthor(author:IAuthor){
    this.provider.getSelectedAuthor(author).then(res=>{
      this.selectedAuthor=res;
      console.log('ok');
      this.globalName=this.selectedAuthor.name+" "+this.selectedAuthor.surname;
    })
  }
  gclick(){
    this.genreclicked=true;
    this.authorclicked=false;
    this.bookcliked=false;
    this.reviewclicked=false;
  }
  bclick(){
    this.genreclicked=false;;
    this.authorclicked=false;
    this.bookcliked=true;
    this.reviewclicked=false;
  }
  aclick(){
    this.genreclicked=false;
    this.authorclicked=true;
    this.bookcliked=false;
    this.reviewclicked=false;
  }
  rclick(){
    this.genreclicked=false;
    this.authorclicked=false;
    this.bookcliked=false;
    this.reviewclicked=true;
  }
  createBook() {
    const newBook: IBook = {id:this.bookId,title:this.bookName,description:this.bookDescription,page_amount:this.bookPages,year:this.bookYear,category:this.selectedGenre,author:this.selectedAuthor,added_by:this.currentup,image:null};
    this.provider.createBook(newBook).then(res=>{
      this.books.push(res);
      console.log("kek")
    })
  }

  createCategory(){
    if (this.name !== '' ) {
      this.provider.createCategory(this.name).then(res => {
        this.name = '';
        this.genres.push(res);
      });
    }
  }
  createAuthor(){
     if (this.aname !== '' && this.asurname!=='' && this.adb!=='' && this.add!=='' ) {
        this.provider.createAuthor(this.aname,this.asurname,this.adb,this.add).then(res => {
        this.aname='';
        this.asurname='';
        this.adb='';
        this.add='';
        this.authors.push(res);
      });
    }
  
    console.log("kej")
    
  }
  deleteBook(){
    this.provider.deleteBook(this.selectedBook).then(res=>{
      this.provider.getUserBook(this.currentup).then(res=>{
        this.books=res;
      })
    })
  }
  deleteAuthor(){
    this.provider.deleteAuthor(this.selectedAuthor).then(res=>{
      this.provider.getAuthors().then(res=>{
        this.authors=res;
      })
    })
  }
  deleteGenre(){
    this.provider.deleteGenre(this.selectedGenre).then(res=>{
      this.provider.getCategories().then(res=>{
        this.genres=res;
      })
    })
  }
  signup(){
    this.signed=true;
      this.provider.signup(this.slogin,this.spassword,this.semail).then(res=>{
        this.provider.auth(this.slogin,this.spassword).then(r => {
          localStorage.setItem('token', r.token);
          this.logged = true;
      });
    });
  }

}
