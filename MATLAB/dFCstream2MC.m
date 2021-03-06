function MC = dFCstream2MC(dFCstream)

% FUNCTION MC = dFCstream2MC(dFCstream)
% takes dFCstream as input ('2D' or '3D') and calculates meta-connectivity 
% (MC) [lxl] matrix, where l is the number of edges in the input dFCstream.
% MC represents correlation between pair of edges.
%
% input: dFCstream --> generated by TS2dFCstream (2D or 3D)
%
% Example: mc = dFCstream2MC(dfcstream)
%
% Reference: Lucas Arbabyazd et al. (2020) MethodsX

if (ndims(dFCstream) == 3)
    FCstr = Matrix2Vec(dFCstream);
end

if (ndims(dFCstream) == 2)
    FCstr = dFCstream;
end

if size(dFCstream,1) > 20000
    disp('Caution! If number of your parcellation > 200 regions, this')
    disp('function may take one minutes, instead you can only calculate')
    disp('trimers of MC, using dFCstream2Tri function!')
    return
end
MC=corr(FCstr');
MC=MC-eye(size(MC,1));


