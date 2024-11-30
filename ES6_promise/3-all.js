import { createUser, uploadPhoto } from './utils';

function handleProfileSignup() {
  const arr = [uploadPhoto(), createUser()];
  Promise.all(arr).then((data) => { console.log(`${data[0].body} ${data[1].firstName} ${data[1].lastName}`); }).catch(() => { console.log('Signup system offline'); });
}

export default handleProfileSignup;
