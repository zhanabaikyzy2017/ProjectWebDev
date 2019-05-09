import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { LoginComponent} from './login/login.component';
import { AllpageComponent } from './allpage/allpage.component';

const routes: Routes = [
  { path: '', component:MainComponent},
  {path:'login',component:LoginComponent},
  {path:'easyLib',component:AllpageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
