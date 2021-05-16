class HttpException extends Error {
    status: number;
    message: string;
    constructor(status: number = 500, message: string = 'Internal server error.') {
      super(message);
      this.status = status;
      this.message = message;
    }
  }
   
  export default HttpException;