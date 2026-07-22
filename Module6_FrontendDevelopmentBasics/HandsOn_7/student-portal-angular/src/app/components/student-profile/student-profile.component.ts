import {Component} from '@angular/core';
import {CommonModule} from '@angular/common';
import {ReactiveFormsModule, FormGroup, FormControl, Validators} from '@angular/forms';

@Component({
  selector:'app-student-profile',
  standalone:true,
  imports:[CommonModule, ReactiveFormsModule],
  templateUrl:'./student-profile.component.html',
  styleUrl:'./student-profile.component.css'
})
export class StudentProfileComponent{
  profileForm=new FormGroup({
    name:new FormControl('Alex Johnson', [Validators.required]),
    email:new FormControl('alex.j@university.edu', [Validators.required, Validators.email]),
    semester:new FormControl(6, [Validators.required, Validators.min(1), Validators.max(8)])
  });

  onSubmit():void{
    if(this.profileForm.valid){
      console.log('Form Submitted Successfully:', this.profileForm.value);
    }
  }
}