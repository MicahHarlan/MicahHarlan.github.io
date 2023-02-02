import { ActiveDescendantKeyManager } from '@angular/cdk/a11y';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import {NgForm} from '@angular/forms';

@Component({
  selector: 'app-contact-form',
  templateUrl: './contact-form.component.html',
  styleUrls: ['./contact-form.component.css']
})
export class ContactFormComponent implements OnInit {

  @Input() name = "First Name"
  @Input() lastName1 = "Last Name"
  @Input() comment = "User Comment"
  
  
  @Output() newValsEvent = new EventEmitter<{name: string, lastName1: string}>()
  @Output() newCommentEvent = new EventEmitter<string>()

  constructor() { }

  ngOnInit(): void {
  }

  toDict(name: string, lastName: string){
   let dict = {name: name,lastName: lastName}
   this.addValues2(dict)
  }

  addValues2(dict: {name: string, lastName: string}){
    let name = dict['name']
    let lastName = dict['lastName']
    this.newValsEvent.emit({name:dict['name'], lastName1: dict['lastName']})   
  
  }

  makeComment(input: string){
    this.newCommentEvent.emit(input)
    console.log()
  }

}



