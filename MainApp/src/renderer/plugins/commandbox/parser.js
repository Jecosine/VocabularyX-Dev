/*
 * @Date: 2021-02-15 13:33:14
 * @LastEditors: Jecosine
 * @LastEditTime: 2021-02-18 13:45:23
 */
import CommandParseException from '../../exceptions/CommandParseException'

const parser = {
  configuration: null,
  parse: (raw, mapper) => {
    var commandData
    console.log('in parser')
    console.log(`parsing command ${raw}`)
    if (raw && (typeof (raw) === 'string')) {
      if (raw[0] === '/') {
        commandData = parser.grammarCheck(raw, mapper)
      } else {
        throw new CommandParseException(`Invalid Command, aborting`)
      }
    }
    console.log('parsed')
    return commandData
  },
  // getOptionConfig (optName) {
  //   parser.configuration.opts.forEach(element => {
  //     if (element.name === optName) {

  //     }
  //   });
  // },
  checkParam (param) {
    let opts = parser.configuration['opts']
    console.log('in checkParam')
    console.log(parser.configuration, parser.configuration['opts'])
    let keys = Object.keys(opts)
    for (let i = 0; i < keys.length; ++i) {
      let key = keys[i]
      if (opts[key].long === param || opts[key].short === param) {
        console.log(`In parser: Match param ${key}`)
        return key
      }
    }

    return false
  },
  grammarCheck (raw, mapper) {
    // let commandGroup = raw.trim().split(' ')
    // remove blank chars on both sides
    raw = raw.trim()
    let prinReg = /\/([\w]+)/
    let principalMatch = raw.match(prinReg)
    let principal = principalMatch[1].trim()
    // get command configuration
    parser.configuration = (mapper[principal]) ? mapper[principal]['configuration'] : undefined
    // testcode
    // parser.configuration = {
    //   name: 'test',
    //   opts: {
    //     param1: {
    //       name: 'param1',
    //       type: 'string',
    //       short: '-p1',
    //       long: '--param1',
    //       require: false
    //     },
    //     param2: {
    //       name: 'param2',
    //       type: 'boolean',
    //       short: '-p2',
    //       long: '--param2',
    //       require: true
    //     }
    //   }
    // }

    if (parser.configuration === undefined) {
      throw new CommandParseException(`Command ${principal} not exists`)
    }
    // generate command checker
    let opts = {}
    // Object.keys(parser.configuration.opts).forEach((element, i) => {
    //   opts[element] = null
    // })
    // parse option
    // if (!parser.configuration) {
    //   throw new CommandParseException(`Command ${principal} is not configured`)
    // } else {
    //   parser.configuration = null
    //   console.log(`fetching configuration of ${principal}`)
    // }
    let optStr = raw.slice(principalMatch[0].length).trim()
    let paramReg = /-{1,2}([\w]+)/
    let valueReg = /[\S]+/
    let paramMatch = optStr.match(paramReg)
    let valueMatch = null
    while (paramMatch) {
      if (paramMatch.index !== 0) {
        throw new CommandParseException(`Invalid command`)
      }
      console.log(`Match param: ${paramMatch}`)
      // check whether parameter exists
      let param = parser.checkParam(paramMatch[0])
      if (!param) {
        throw new CommandParseException(`Parameter ${paramMatch[0]} not exists`)
      }
      let paramType = parser.configuration.opts[param].type
      optStr = optStr.slice(paramMatch[0].length).trim()
      // parse value
      valueMatch = optStr.match(valueReg)
      if (valueMatch.index !== 0) {
        throw new CommandParseException(`Invalid command`)
      }
      if (valueMatch) {
        let val = valueMatch[0].trim()
        let tempVal = val.trim()
        console.log(`get value of ${param} : ${tempVal}`)
        try {
          tempVal = (paramType === 'boolean') ? !!((val && (val !== '0' || val !== 'false'))) : tempVal
        } catch (e) {
          throw new CommandParseException(`Parameter ${param} value error, cannot convert ${val} to type ${paramType}`)
        }
        opts[param] = tempVal
        optStr = optStr.slice(valueMatch[0].length).trim()
      }
      paramMatch = optStr.match(paramReg)
    }
    // check require field
    // ...
    return {
      name: principal,
      opts: opts
    }
    // parse string
  }
}

export default parser
