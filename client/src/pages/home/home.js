import React, { Component, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useState } from "react";
import "./home.css";
import xeniadark from "../../assets/images/Xeniadark.png";
import bgcricwars3 from "../../assets/images/cricwarshomepage3.png";
import bgcricwars1 from "../../assets/images/cricwarshomepage1.png";
import bgcricwars2 from "../../assets/images/cricwarshomepage2.png";
const Home = () => {

  const [canRate, setCanRate] = useState(false);
  const [canView, setCanView] = useState(false);
  const [canCreate, setCanCreate] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const fetchData = () => {
    console.log(localStorage.getItem("auth-token"));
    fetch("http://localhost:8000/users/me",{
      method: "GET",
      headers: { "content-type": "application/json", "Authorization":`Token ${localStorage.getItem("auth-token")}` },
    })
      .then(response => {
        return response.json()
      })
      .then(data => {
        console.log(data)
        setCanRate(data.canRatePlayers);
        setCanView(data.canAccessFinalRatings);
        setCanCreate(data.canSelectTeam);
        // setPlayerArray(data)
      })
  }

  const checkAuth = () => {
    if(localStorage.getItem("auth-token") === null) setIsAuthenticated(false);
    else setIsAuthenticated(true);
  }

  useEffect(() => {
    
    checkAuth();
    fetchData();
  }, [])

  return (
    <div>
      <div className="container-home">
        <div>
          <img
            className="homepage-background-img relative "
            // src={bgcricwars3}
            src={bgcricwars1}
            // src={bgcricwars2}
            alt="homepage-background"
          />
        </div>
        <div>
          <img
            classname="xeniadark pb-24 absolute px-48 py 12"
            src={xeniadark}
            alt="logo"
          />
        </div>
        <Link to="/login">
          <button
            type="submit"
            className="btn py-3  px-8 hover:text-teal-200 inline-block text-lg absolute text-center  text-white bg-gradient-to-r from-blue-400 via-purple-500 to-violet-400 hover:bg-gradient-to-br  focus:outline-none focus:ring-red-300 dark:focus:ring-red-800   "
          >
            Click to Login
          </button>
        </Link>

        {!isAuthenticated && (
          <Link to="/login">
            <button
              type="submit"
              className="btn py-3 px-8 hover:text-teal-200 inline-block text-lg absolute text-center  text-white bg-gradient-to-r from-blue-400 via-purple-500 to-violet-400 hover:bg-gradient-to-br  focus:outline-none focus:ring-red-300 dark:focus:ring-red-800   "
            >
              Click to Login
            </button>
          </Link>
        )}
        {canRate && (
          <Link to="/ratings">
            <button
              type="submit"
              className="btn py-3 px-8 hover:text-teal-200 inline-block text-lg absolute text-center  text-white bg-gradient-to-r from-blue-400 via-purple-500 to-violet-400 hover:bg-gradient-to-br  focus:outline-none focus:ring-red-300 dark:focus:ring-red-800   "
            >
              Rate Players
            </button>
          </Link>
        )}
        {canCreate && (
          <Link to="/create-team">
            <button
              type="submit"
              className="btn py-3 px-8 hover:text-teal-200 inline-block text-lg absolute text-center  text-white bg-gradient-to-r from-blue-400 via-purple-500 to-violet-400 hover:bg-gradient-to-br  focus:outline-none focus:ring-red-300 dark:focus:ring-red-800   "
            >
              Create Team
            </button>
          </Link>
        )}
      </div>
    </div>
  );
};

export default Home;



