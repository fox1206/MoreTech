import React from "react";
import { Card } from "@mui/material";
import { CardHeader } from "@mui/material"; 
import { CardContent } from "@mui/material";
import EventDiscription from "./EventDiscription";

export default function Events() {
  const list = [
      {id: 1, title: "Курсы менеджеров", discription: "Какое-то описание событияКакое-то описание события"},
      {id: 1, title: "Курсы менеджеров", discription: "Какое-то описание событияКакое-то описание события"},
  ]
  return (
      <Card sx={{ 
        minWidth: 300,
        padding: '24px',
        borderRadius: '12px',
        backgroundColor: '#252A41',
        color: '#FFFFFF',
        }}>
          <CardHeader sx={{padding: '0 0 32px 0'}} title={"Предстоящие события"} 
        subheader="Все"
        subheaderTypographyProps={{                
              fontSize: 14,
              color: '#818CF8',
              position: 'relative',
              top: -27,
              align: 'right'
            }}
      />
          <CardContent sx={{padding: 0,
              display: 'flex',
              overflow: 'hidden'
          }}>
            <EventDiscription list={list}/>
          </CardContent>
      </Card>
  );
}