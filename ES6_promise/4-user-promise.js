function signUpUser(firstName, lastName) {
  const obj = {
    firstName,
    lastName,
  };
  const p = new Promise((resolve) => { resolve(obj); });
  p.then();
  return p;
}

export default signUpUser;
