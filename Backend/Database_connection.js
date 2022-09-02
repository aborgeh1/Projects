export function Database()
{return
    mongoose.connect("mongodb://127.0.0.1:27017/aborgeh",
    {
        useNewUrlParser:true,
        useUnifiedTopology:true
    }
).then(gh=>console.log('connection is successsfull')).catch(err=>console.log(err, 'ERROR OCCURED'))
const app= express();
}