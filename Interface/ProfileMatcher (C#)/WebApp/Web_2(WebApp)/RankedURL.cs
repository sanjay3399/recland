using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Web_2_WebApp_
{
    class RankedURL
    {
        int rank;
        Dictionary<string, Dictionary<string, int>> wordPerURLCount;

        public RankedURL(int rank, Dictionary<string, Dictionary<string, int>> wordPerURLCount)
        {
            this.rank = rank;
            this.wordPerURLCount = wordPerURLCount;
        }

        public int Rank
        {
            get { return rank; }
            set { rank = value; }
        }

        public Dictionary<string, Dictionary<string, int>> WordPerURLCount
        {
            get { return wordPerURLCount; }
            set { wordPerURLCount = value; }
        }
    }
}