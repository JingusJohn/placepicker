
import React from 'react'


const Fruits = async ({ }: any) => {
  const userDataRaw = await fetch('http://localhost:8000/users');
  const userData = await userDataRaw.json();
  console.log("api fetched: ", userData)
  let fruitDisplay = userData.map((user: any) => {
    return <div>
      <h1 className="text-2xl">{user.name}</h1>
      <div className="flex flex-col pl-4">
        <h2 className="text-lg">{user.favorite_fruit.name}</h2>
        <p>{user.favorite_fruit.sweetness}</p>
      </div>
    </div>
  });
  return (
    <div className="flex flex-col space-y-2 px-4">
      <h1>Our users' favorite fruits!</h1>
      <div className="flex flex-col space-y-2">{fruitDisplay}</div>
    </div>
  )
}

export default Fruits
