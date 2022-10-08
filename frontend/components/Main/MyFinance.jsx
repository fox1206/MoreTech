import React from "react";
import {Card, CardHeader, CardContent, CardActions, Button, Typography} from "@mui/material";
import CachedIcon from '@mui/icons-material/Cached';

export const MyFinance = () => {
  return (
    <>
      <Card sx={{ 
        minWidth: 300 
        }}>
        <CardHeader title={"Мои финансы"} sx={{padding: 0}}/>
        <CardContent sx={{padding: '40px 0 0 0'}}>
               
        </CardContent>
        <CardActions sx={{padding: '40px 0 0 0'}}>
          <Button
            variant="contained"
            startIcon={<CachedIcon />}
          >
          Обменять на рубли</Button>
        </CardActions>
      </Card>
    </>
  )
};