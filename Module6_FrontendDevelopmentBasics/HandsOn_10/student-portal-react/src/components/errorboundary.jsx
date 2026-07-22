import React from 'react';

export default class ErrorBoundary extends React.Component{
  constructor(props){
    super(props);
    this.state={hasError:false, error:null};
  }

  static getDerivedStateFromError(error){
    return {hasError:true, error};
  }

  componentDidCatch(error, errorInfo){
    console.error('Global Error Boundary caught an error:', error, errorInfo);
  }

  render(){
    if(this.state.hasError){
      return (
        <div className='error-box' style={{margin:'2rem auto', maxWidth:'600px', textAlign:'center'}}>
          <h2>An unexpected UI error occurred.</h2>
          <p>{this.state.error?.message || 'Something went wrong.'}</p>
          <button 
            type='button' 
            className='primary-btn' 
            style={{marginTop:'1rem'}}
            onClick={()=>window.location.reload()}
          >
            Reload Application
          </button>
        </div>
      );
    }
    return this.props.children;
  }
}