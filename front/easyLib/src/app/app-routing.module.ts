import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { LoginComponent} from './login/login.component';
import { OneAuthorComponent} from './one-author/one-author.component';
import { OneGenreComponent} from './one-genre/one-genre.component';
import { SignComponent} from './sign/sign.component'


const routes: Routes = [
  { path: '', component:MainComponent},
  {path:'login',component:LoginComponent},
  {path:'author',component:OneAuthorComponent},
  {path:'genre',component:OneGenreComponent},
  {path:'sign',component:SignComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
