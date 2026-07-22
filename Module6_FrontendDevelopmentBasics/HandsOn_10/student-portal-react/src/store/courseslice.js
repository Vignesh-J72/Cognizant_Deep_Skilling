
import {createSlice, createAsyncThunk, createSelector} from '@reduxjs/toolkit';
import {getAllCourses, enrollStudent} from '../api/courseApi';

export const fetchCoursesThunk=createAsyncThunk(
  'courses/fetchAll',
  async(_, {rejectWithValue})=>{
    try{
      return await getAllCourses();
    }catch(err){
      return rejectWithValue(err.message || 'Failed to fetch courses from server');
    }
  }
);

export const enrollCourseThunk=createAsyncThunk(
  'courses/enroll',
  async({studentId, course}, {rejectWithValue})=>{
    try{
      await enrollStudent(studentId, course.id);
      return course;
    }catch(err){
      return rejectWithValue(err.message || 'Failed to enroll in course');
    }
  }
);

const courseSlice=createSlice({
  name:'courses',
  initialState:{
    items:[],
    enrolled:[],
    loading:false,
    error:null
  },
  reducers:{
    unenroll:(state, action)=>{
      state.enrolled=state.enrolled.filter(c=>c.id!==action.payload);
    },
    clearError:(state)=>{
      state.error=null;
    }
  },
  extraReducers:(builder)=>{
    builder
      .addCase(fetchCoursesThunk.pending, (state)=>{
        state.loading=true;
        state.error=null;
      })
      .addCase(fetchCoursesThunk.fulfilled, (state, action)=>{
        state.loading=false;
        state.items=action.payload;
      })
      .addCase(fetchCoursesThunk.rejected, (state, action)=>{
        state.loading=false;
        state.error=action.payload;
      })
      .addCase(enrollCourseThunk.fulfilled, (state, action)=>{
        const exists=state.enrolled.some(c=>c.id===action.payload.id);
        if(!exists){
          state.enrolled.push(action.payload);
        }
      })
      .addCase(enrollCourseThunk.rejected, (state, action)=>{
        state.error=action.payload;
      });
  }
});

export const {unenroll, clearError}=courseSlice.actions;

const selectCourseState=state=>state.courses;

export const selectCourses=createSelector(
  [selectCourseState],
  courseState=>courseState.items
);

export const selectEnrolledCourses=createSelector(
  [selectCourseState],
  courseState=>courseState.enrolled
);

export const selectCoursesLoading=createSelector(
  [selectCourseState],
  courseState=>courseState.loading
);

export const selectCoursesError=createSelector(
  [selectCourseState],
  courseState=>courseState.error
);

export default courseSlice.reducer;