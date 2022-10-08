import React from "react";
import {Typography, Container} from '@mui/material';

const HomePages = ({children}) => {
  return (
    <div>
      <Container maxWidth='xl'>
        <div>
          {children}
        </div>          
      </Container>
    </div>
  );
};

export default HomePages;