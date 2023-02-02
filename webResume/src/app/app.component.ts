import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'LearnSite';
  currentName = "New User"
  lastName =  ""
  show = true
  currentComment = "New Comment"
  pdfSource = "https://vadimdez.github.io/ng2-pdf-viewer/assets/pdf-test.pdf";

  parDict(name: string, lastName: string){
    let dict = {name: name,lastName: lastName}
    this.addVals(dict)
    return dict; 
   }

  addVals(dict: {name: string, lastName: string}) {
    this.currentName = (dict['name'])
    this.lastName= (dict['lastName'])
    this.show = false
    
  }
  setComment(comment: string){
    this.currentComment = (comment)
    console.log(this.currentComment)
  }
  
} 