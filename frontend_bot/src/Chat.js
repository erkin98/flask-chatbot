import React, { useCallback, useEffect, useRef, useState } from "react";
import PersonIcon from '@material-ui/icons/Person';
import { Avatar, makeStyles } from "@material-ui/core";
import { useParams } from "react-router-dom";
import "./Chat.css";
import axios from 'axios';
import { useStateValue } from "./StateProvider";
import Spinner from './Spinner';
const useStyles = makeStyles((theme) => ({
  large: {
    width: "50px",
    height: "50px",
  },
}));

function Chat() {
  const { roomId } = useParams();
  const [messages, setMessages] = useState([]);
  const [state,dispatch] = useStateValue();
  const [loading, setLoading] = useState(true);
  const size = useRef(10);
  const classes = useStyles();
  const divRef = useRef(null);
  // for hide load more div when no more messages
  const spinner = useRef(true);
  // check first click to prevent appling puf effect to first messages
  const fetched = useRef(false);
  const messagesRef = document.getElementsByClassName('messages');
  const fetchData = useCallback(async() => {
    try{
      setLoading(true);
      const res = await axios.post('/customers/'+state.customers[roomId],{size:size.current});
      if(res?.data?.data?.slice(size.current-10).length < 10 ){
        document.querySelector(".chat__size").style.display = "none"; 
        spinner.current = false;
      }else{
        document.querySelector(".chat__size").style.display = "block"; 
        spinner.current = true;
      }
      if(size.current >10){
        setMessages((prev)=> [...res?.data?.data?.slice(size.current-10).reverse(),...prev]);
        if(fetched.current){
          for(let i = 0; i < res?.data?.data?.slice(size.current-10).length*2;i++){
            messagesRef[i].classList.add('new-msg');
          }
          setTimeout(()=>{
            for(let i = 0; i < res?.data?.data?.slice(size.current-10).length*2;i++){
              messagesRef[i].classList.remove('new-msg');
            } 
          },2000);
        }
      }
      else{ 
        setMessages(res?.data?.data?.reverse());
      }
      divRef.current.removeEventListener('DOMNodeInserted', nodeInserted);
      setLoading(false);
      return res;
    }catch(err){ 
      setLoading(false);
      divRef.current.removeEventListener('DOMNodeInserted', nodeInserted);
      return err; 
    }

  },[roomId,state.customers]);

  const fetchPrevious = ()=>{
    size.current +=10;
    fetched.current = true;
    dispatch({ type: "UPDATE_SIZE", size: size.current });
    fetchData();
  }

  useEffect(() => {
      setMessages([]);
      size.current = 10;
      divRef.current.addEventListener('DOMNodeInserted', nodeInserted);
      fetchData();
  }, [roomId,fetchData]);
  
  const nodeInserted = event => {
    const { currentTarget } = event;
    currentTarget.scroll({ top: currentTarget.scrollHeight, behavior: 'smooth' });
  }

  useEffect(() => {
    const reference = divRef.current;
    const listenScroll = ()=>{
      const winScroll =reference.scrollTop;
      if(winScroll < 10 && spinner.current){
        document.querySelector(".chat__size").style.display = "block";
      }else{
        document.querySelector(".chat__size").style.display = "none";
      }
    }
    if (divRef) {
      reference.addEventListener('scroll', listenScroll);
    }
    return ()=> reference.removeEventListener("scroll",listenScroll);
  }, []);

  return (
    <div className="chat">
      <div className="chat__header">
        <div className="chat__header__left">
          <div className="chat__header__info">
              <Avatar
              src={<PersonIcon/>}
              className={classes.large}
            />
            <h3>{state.customers[roomId]}</h3>
          </div>
        </div>
      </div>
      <div className="chat__body" ref={divRef}>
        <div className="chat__size"> 
            <div className="chat__size__inner">
              {loading ? <Spinner/> : <div className="chat__size__icon" onClick={fetchPrevious}>+10</div>}
              
            </div>
        </div>
        {messages?.map((mes) => {
          return mes?.map((s,idx)=>
            <div key={`msg-${idx}`} className="messages">
              <p
            className={`chat__message ${
              mes?.indexOf(s) === 1 && "chat__reciever"
            }`}
          >
            {s}
          </p>
          </div>
        )
        })}
      </div>
    </div>
  );
}

export default Chat;
