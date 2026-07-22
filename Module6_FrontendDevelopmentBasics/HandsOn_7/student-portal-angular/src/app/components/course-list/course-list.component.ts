import {Component, OnInit, OnDestroy} from '@angular/core';
import {CommonModule} from '@angular/common';
import {FormsModule} from '@angular/forms';
import {Subscription} from 'rxjs';
import {Course} from '../../models/course.model';
import {CourseService} from '../../services/course.service';
import {CourseCardComponent} from '../course-card/course-card.component';

@Component({
  selector:'app-course-list',
  standalone:true,
  imports:[CommonModule, FormsModule, CourseCardComponent],
  templateUrl:'./course-list.component.html',
  styleUrl:'./course-list.component.css'
})
export class CourseListComponent implements OnInit, OnDestroy{
  courses:Course[]=[];
  searchTerm:string='';
  loading:boolean=true;
  private courseSub!:Subscription;

  constructor(private courseService:CourseService){}

  ngOnInit():void{
    this.loading=true;
    this.courseSub=this.courseService.getCourses().subscribe({
      next:(data)=>{
        this.courses=data;
        this.loading=false;
      },
      error:()=>{
        this.loading=false;
      }
    });
  }

  get filteredCourses():Course[]{
    return this.courses.filter(course=>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
      course.code.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }

  trackByCourseId(index:number, course:Course):number{
    return course.id;
  }

  ngOnDestroy():void{
    if(this.courseSub){
      this.courseSub.unsubscribe();
    }
  }
}