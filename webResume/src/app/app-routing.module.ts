import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ResumeComponent } from './resume/resume.component';
import { ContactFormComponent } from './contact-form/contact-form.component';
import { AppComponent } from './app.component';
import { ExperienceComponent } from './experience/experience.component';
const routes: Routes = [
  {path: 'Resume', component: ResumeComponent},
  {path: 'Home', component: AppComponent},
  {path: 'Contact',component: ContactFormComponent},
  {path: 'Experience', component: ExperienceComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

