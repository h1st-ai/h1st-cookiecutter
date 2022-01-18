import React from 'react';
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            text:'',
            output: ''
        }
        this.handleInputChange = this.handleInputChange.bind(this)
        this.translate = this.translate.bind(this)
    }

    handleInputChange(event) {
        const target = event.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;
        this.setState({
            [name]: value    });
    }

    translate(event) {
        event.preventDefault();
        axios.post('/api/v1/translate/', {
            'text': this.state.text,
            'input_language': 'english',
            'output_language': 'english'
        }).then(result => {
            this.setState({output: result.data.output})
        })
    }

    render() {
        return (
            <div className="container">
                <header className="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
                    <a href="/"
                       className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                        <span className="fs-4">Language Translator</span>
                    </a>
                </header>

                <div className="row">
                    <div className="col">
                        <form onSubmit={this.translate}>
                            <label htmlFor="inputText" className="form-label">Text to be translated</label>
                                <textarea className="form-control" name='text' id='inputText' rows="3"
                                          value={this.state.text} onChange={this.handleInputChange}/>
                            <br/>
                            <input type="submit" className="btn btn-primary mb-3" value="Translate"/>
                        </form>
                    </div>
                    <div className="col">
                        <label className="form-label">Result:</label>
                        <div className="h-50 bg-light">
                            {this.state.output}
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default App;