import React, { Component, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useState } from "react";
import bgcricwars3 from "../../assets/images/cricwarshomepage3.png";
import bgcricwars1 from "../../assets/images/cricwarshomepage1.png";
import bgcricwars2 from "../../assets/images/cricwarshomepage2.png";
const Home = () => {

  const [canRate, setCanRate] = useState(false);
  const [canView, setCanView] = useState(false);
  const [canCreate, setCanCreate] = useState(false);
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

  useEffect(() => {
    fetchData();
  }, [])

  return (
    <div>
      <div>
        <img
          className="homepage-background-img earth"
          src={bgcricwars3}
          // src={bgcricwars1}
          // src={bgcricwars2}
          alt="homepage-background"
        />
        {canRate && (
          <Link to="/ratings">
            <button class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
              Rate Players
            </button>
          </Link>
        )}
        {canView && (
          <Link to="/ratings">
            <button class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
              View Ratings
            </button>
          </Link>
        )}
        {canCreate && (
          <Link to="/create-team">
            <button class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
              Create Team
            </button>
          </Link>
        )}
      </div>
    </div>
  );
};

export default Home;



